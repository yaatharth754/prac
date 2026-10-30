
import heapq

class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None

def printCodes(root, code=""):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.ch, ":", code if code else "0", "| Value:", root.freq)
        return

    printCodes(root.left, code + "0")
    printCodes(root.right, code + "1")


n = int(input("Enter the number of characters: "))

pq = []
vertices = 0

for i in range(n):
    ch, freq = input().split()
    heapq.heappush(pq, (int(freq), vertices, Node(ch, int(freq))))
    vertices += 1

while len(pq) > 1:
    freq1, _, left = heapq.heappop(pq)
    freq2, _, right = heapq.heappop(pq)

    parent = Node('\0', freq1 + freq2)
    parent.left = left
    parent.right = right

    heapq.heappush(pq, (parent.freq, vertices, parent))
    vertices += 1

root = pq[0][2]

print("\nHuffman Codes and Values:")
printCodes(root)

print("\nTotal Vertices:", vertices)
print("Root Value:", root.freq)


# 4
# A 5
# B 9
# C 12
# D 13
# #include <iostream>
# #include <queue>
# #include <vector>
# #include <string>
# using namespace std;

# struct Node {
#     char ch;
#     int freq;
#     Node *left, *right;

#     Node(char c, int f) : ch(c), freq(f), left(nullptr), right(nullptr) {}
# };

# struct Compare {
#     bool operator()(Node* a, Node* b) {
#         return a->freq > b->freq;
#     }
# };

# void printCodes(Node* root, string code) {
#     if (root == nullptr)
#         return;

#     if (root->left == nullptr && root->right == nullptr) {
#         cout << root->ch << ": " << (code.empty() ? "0" : code) << endl;
#         return;
#     }

#     printCodes(root->left, code + "0");
#     printCodes(root->right, code + "1");
# }

# int main() {
#     int n;
#     cout <<"Enter the number of characters: ";
#     cin >> n;

#     if (n <= 0)
#         return 0;

#     priority_queue<Node*, vector<Node*>, Compare> pq;

#     for (int i = 0; i < n; i++) {
#         char ch;
#         int freq;
#         cin >> ch >> freq;
#         pq.push(new Node(ch, freq));
#     }

#     while (pq.size() > 1) {
#         Node* left = pq.top();
#         pq.pop();

#         Node* right = pq.top();
#         pq.pop();

#         Node* parent = new Node('\0', left->freq + right->freq);
#         parent->left = left;
#         parent->right = right;

#         pq.push(parent);
#     }

#     printCodes(pq.top(), "");

#     return 0;
# }


