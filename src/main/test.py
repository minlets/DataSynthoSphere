# tracer.py
import sys
import trace
import App

def trace_calls(frame, event, arg):
    if event == 'call':
        func_name = frame.f_code.co_name
        file_name = frame.f_code.co_filename
        print(f"Function '{func_name}' is called from '{file_name}'.")
    return trace_calls

if __name__ == "__main__":
    # Import the script you want to trace
    import App

    # Set up the trace
    sys.settrace(trace_calls)

    # Execute the script (example.py)
    App.main()
