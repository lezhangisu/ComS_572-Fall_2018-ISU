# -*- coding: UTF-8 -*-

import sys, time

class ShowProcess():
    """
    Progress bar class
    """
    i = 0 # current progress
    max_steps = 0 # total steps
    max_arrow = 50 # max length of the progress bar
    infoDone = 'done'

    # Initialization, takes in totoal steps and done info
    def __init__(self, max_steps, infoDone = 'Done'):
        self.max_steps = max_steps
        self.i = 0
        self.infoDone = infoDone

    # show progress
    # Effect: [>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
    def show_process(self, i=None):
        if i is not None:
            self.i = i
        else:
            self.i += 1
        num_arrow = int(self.i * self.max_arrow / self.max_steps) # calculate num of '>'
        num_line = self.max_arrow - num_arrow # calculate num of '-'
        percent = self.i * 100.0 / self.max_steps # calculate percentage, format: xx.xx%
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r' # output string，'\r' means do not create new line
        sys.stdout.write(process_bar) # print to screen
        sys.stdout.flush()
        if self.i >= self.max_steps:
            self.close()

    def close(self):
        print('')
        print(self.infoDone)
        self.i = 0

if __name__=='__main__':
    max_steps = 30

    print "Some Title"
    process_bar = ShowProcess(max_steps, 'Done')

    for i in range(max_steps):
        process_bar.show_process()
        time.sleep(0.05)
