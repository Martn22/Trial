#!/usr/bin/env python3
import cmd

class HBNBCommand(cmd.Cmd):
        prompt = '(hbnb) '


        def do_quit(self, arg):
            """quit the command line interface"""
            return True

        def do_EOF(self, arg):
            """quit interface o EOF"""
            return True

if __name__ == '__main__':
        HBNBCommand().cmdloop()
