#include <iostream>
#include <stack>
#include <string>

struct Bracket {
    Bracket(char type, int position):
        type(type),
        position(position)
    {}

    bool Matchc(char c) {
        if (type == '[' && c == ']')
            return true;
        if (type == '{' && c == '}')
            return true;
        if (type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
};

int main() {
    std::string text;
    getline(std::cin, text);
    int pos = 0;

    std::stack <Bracket> opening_brackets_stack;
    for (int position = 0; position < text.length(); ++position) {
        char next = text[position];

        if (next == '(' || next == '[' || next == '{') {
            // Process opening bracket, write your code here
            Bracket *b = new Bracket(next, position + 1);
            opening_brackets_stack.push(*b);
        }
        // std::cout<<position<<std::endl;
        // std::cout<<next<<std::endl;
        if (next == ')' || next == ']' || next == '}') {
            // Process closing bracket, write your code here
            if (opening_brackets_stack.size() == 0) {
                pos = position + 1;
                break;
            } else if (opening_brackets_stack.top().Matchc(next)) {
                opening_brackets_stack.pop();
            } else {
                pos = position + 1;
                break;
            }
        }
    }

    // Printing answer, write your code here
    if (pos == 0 & opening_brackets_stack.size() == 0) {
        std::cout<<"Success"<<std::endl;
    } else {
        if (pos == 0 & opening_brackets_stack.size() != 0) {
          pos = opening_brackets_stack.top().position;
        }
        std::cout<<pos<<std::endl;
    }

    return 0;
}
