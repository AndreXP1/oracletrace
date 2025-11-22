import sys
import os
import time
from collections import defaultdict
from rich.tree import Tree
from rich import print

_enabled = False
_root_path = ""
_call_stack = []  
_func_calls = defaultdict(int)
_func_time = defaultdict(float)
_call_map = defaultdict(lambda: defaultdict(int))

def _is_user_code(filename):
    if not filename.startswith(_root_path):
        return False
    if "site-packages" in filename or "dist-packages" in filename:
        return False
    return True

def _get_key(frame):
    co_filename = frame.f_code.co_filename
    if co_filename.startswith("<"):
        return None
    filename = os.path.abspath(co_filename)
    if not _is_user_code(filename):
        return None
    rel_path = os.path.relpath(filename, _root_path)
    return f"{rel_path}:{frame.f_code.co_name}"

def _trace(frame, event, arg):
    if not _enabled:
        return
    
    if event == "call":
        key = _get_key(frame)
        if not key:
            return
        
        caller = _call_stack[-1][1] if _call_stack else "<module>"
        _call_map[caller][key] += 1
        _func_calls[key] += 1
        _call_stack.append((id(frame), key, time.perf_counter()))
        
    elif event == "return":
        if not _call_stack:
            return
        
        if id(frame) == _call_stack[-1][0]:
            _, key, start = _call_stack.pop()
            _func_time[key] += time.perf_counter() - start
        else:
            fid = id(frame)
            found = False
            for i in range(len(_call_stack) - 1, -1, -1):
                if _call_stack[i][0] == fid:
                    found = True
                    break
            
            if found:
                while _call_stack:
                    top_fid, key, start = _call_stack.pop()
                    _func_time[key] += time.perf_counter() - start
                    if top_fid == fid:
                        break

def start_trace(root_dir):
    global _enabled, _root_path, _call_stack, _func_calls, _func_time, _call_map
    _root_path = os.path.abspath(root_dir)
    _call_stack = []
    _func_calls = defaultdict(int)
    _func_time = defaultdict(float)
    _call_map = defaultdict(lambda: defaultdict(int))
    _enabled = True
    sys.setprofile(_trace)

def stop_trace():
    global _enabled
    _enabled = False
    sys.setprofile(None)

def show_results():
    if not _func_calls:
        print("[yellow]No calls traced.[/]")
        return

    print("\n[bold green]Logic Flow:[/]")
    
    tree = Tree("[bold yellow]<module>[/]")
    
    def add_nodes(parent_node, parent_key, current_path):
        children = _call_map.get(parent_key, {})
        sorted_children = sorted(children.items(), key=lambda x: _func_time[x[0]], reverse=True)
        
        for child_key, count in sorted_children:
            total_time = _func_time[child_key]
            if child_key in current_path:
                parent_node.add(f"[red]↻ {child_key}[/] ({count}x)")
                continue
                
            node_text = f"{child_key} [dim]({count}x, {total_time:.4f}s)[/]"
            child_node = parent_node.add(node_text)
            add_nodes(child_node, child_key, current_path | {child_key})

    add_nodes(tree, "<module>", {"<module>"})
    print(tree)
