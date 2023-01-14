class Solution:
    def interpret(self, command: str) -> str:
        string = ""
        for i in range(len(command)):
            if command[i] == "G":
                string = string + "G"
            elif command[i] == "(" and command[i+1] == ")":
                string = string + "o"
            elif command[i] == "(" and command[i+1] == "a":
                string = string + "al"
        return string