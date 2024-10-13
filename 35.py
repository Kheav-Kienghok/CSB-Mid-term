from multiprocessing import Process, current_process

def show_process_name():
    print("Process name:", current_process().name)

if __name__ == '__main__':
    # Create and start the process
    
    p = Process(target = show_process_name)
    p.start()