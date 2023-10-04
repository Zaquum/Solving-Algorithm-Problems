#include <vector>

class MyListNode {
public:
    int key, value;
    MyListNode* next;

    MyListNode(int key, int value) : key(key), value(value), next(nullptr) {}
};

class MyHashMap {
private:
    int size;
    std::vector<MyListNode*> table;

    int index(int key) {
        return key % size;
    }
public:
    MyHashMap() {
        size = 1000; 
        table = std::vector<MyListNode*>(size, nullptr);
    }
        
    void put(int key, int value) {
        int idx = index(key);
        if (!table[idx]) {
            table[idx] = new MyListNode(key, value);
            return;
        }
        MyListNode* current = table[idx];
        while (current) {
            if (current->key == key) {
                current->value = value;
                return;
            }
            if (!current->next) {
                current->next = new MyListNode(key, value);
                return;
            }
            current = current->next;
        } 
    }
        
    int get(int key) {
        int idx = index(key);
        MyListNode* current = table[idx];
        while (current) {
            if (current->key == key) {
                return current->value;
            }
            current = current->next;
        }
        return -1;            
    }
        
    void remove(int key) {
        int idx = index(key);
        MyListNode* current = table[idx];
        if (!current) {
            return;
        }
        if (current->key == key) {
            table[idx] = current->next;
            delete current;
            return;
        }
        while (current->next) {
            if (current->next->key == key) {
                MyListNode* temp = current->next;
                current->next = current->next->next;
                delete temp;
                return;
            }
            current = current->next;
        }            
    }
};



/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */