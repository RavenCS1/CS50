#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node* next;
} node;

int mian(int argc, char* argv[])
{
    node* list=NULL;
    for (int i=1;i<argc;i++)
    {
       int number=atoi(argv[i]);
       node *n=malloc(sizeof(node));
       if (n==NULL)
       {
            return 1;
       }
       n->number=number;
       n->next=NULL;
       if (list==NULL)
       {
            list=n;
       }
       else if (n->number<list->number)
       {
            n->next=list;
            list=n;
       }
       else
       {
            for (node *ptr=list;ptr!=NULL;ptr=ptr->next)
            {
                if (ptr->next==NULL)
                {
                    ptr->next=n;
                    break;
                }
            }
        }
    }
}

