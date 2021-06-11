//方法1
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution 
{

public:
    Node* copyRandomList(Node* head)
    {
        return bfs(head);
    }

private:
    Node* bfs(Node* head)
    {
        if(!head) return NULL;
        Node* clone = new Node(head->val, NULL, NULL);
        unordered_map<Node*, Node*> visited;
        visited[head] = clone;
        queue<Node*> que;
        que.push(head);
        while(!que.empty())
        {
            Node* tmp;
            tmp = que.front();
            que.pop();
            if(tmp->next && !visited[tmp->next])
            {
                visited[tmp->next] = new Node(tmp->next->val, NULL, NULL);
                que.push(tmp->next);
            }
            if(tmp->random && !visited[tmp->random])
            {
                visited[tmp->random] = new Node(tmp->random->val, NULL, NULL);
                que.push(tmp->random);
            }
            visited[tmp]->next = visited[tmp->next];
            visited[tmp]->random = visited[tmp->random];
        }
        return clone;
    }

};


//方法2
class Solution 
{
    unordered_map<Node*, Node*> visited;
    
public:
    Node* copyRandomList(Node* head)
    {
        
        return dfs(head);
    }

private:
    Node* dfs(Node* head)
    {
        if(!head) return NULL;
        if(visited[head]) 
            return visited[head];
        Node *copy = new Node(head->val, NULL, NULL);
        visited[head] = copy;
        copy->next = dfs(head->next);
        copy->random = dfs(head->random);
        return copy;
    }

};
