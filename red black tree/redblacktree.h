#ifndef _RED_BLACK_TREE_H
#define _RED_BLACK_TREE_H

/* Red Black Tree
	Ethan Lyons - 2020
	
	This is a standard red black tree to be used to store arbitrary structs.
	
	The struct is not directly stored in the tree, instead, by adding a tree_elem as a struct member, the tree_elem of the struct is stored.
	
	Any associated integer value can be used as a key by providing a pointer to a function that returns the key given the tree_elem field in the struct.
	
credit to:
	Introduction To Algorithms (3rd ed), Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein.

*/

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

typedef enum _node_color
{
  red = true,
  black = false
} node_color;

/* Tree element. */
typedef struct _tree_elem
{
  node_color color;
  struct _tree_elem *parent;
  struct _tree_elem *left;
  struct _tree_elem *right;
} tree_elem;

typedef int (*get_key_func) (tree_elem *e);

/* Tree. */
typedef struct _tree
{
  tree_elem nil;
  tree_elem *root;
  get_key_func get_key;
} tree;



/* Must be called before any other functions on a struct tree. runs in O(1) */
void rb_init (tree *, get_key_func);

/* Returns the key value given element via the function pointer given in rb_init */
int get_elem_key (tree *, tree_elem *);

/* runs in O(1) */
void tree_left_rotate (tree *, tree_elem *);

/* runs in O(1) */
void tree_right_rotate (tree *, tree_elem *);

/* Replaces node 'u' with node 'v'. runs in O(1) */
void rb_transplant (tree *, tree_elem *, tree_elem *);

/* Maintains red black properties that may be violated after inserted a new node. runs in O(log N)*/
void rb_insert_fixup (tree *, tree_elem *);

/* Maintains red black properties that may be violated after deleting a node. runs in O(log N)*/
void rb_delete_fixup (tree *, tree_elem *);

/* Inserts a new node. runs in O(log N) */
void rb_insert (tree *, tree_elem *);

/* Removes an existing node. runs in O(log N) */
void rb_delete (tree *, tree_elem *);

/* Returns the current maximum key node. runs in O(log N) */
tree_elem * tree_maximum (tree *, tree_elem *);

/* Returns the current minimum key node. runs in O(log N) */
tree_elem * tree_minimum (tree *, tree_elem *);


/* testing */
/* verifies the red black tree invariants. */
bool rb_verify_tree (tree *);

bool rb_verify_node (tree *, tree_elem *, int);

bool rb_verify_path_invariant (int);

bool rb_verify_child_invariant (tree *, tree_elem *);

bool rb_verify_root_invariant (tree *);

bool rb_verify_leaf_invariant (tree *);

bool rb_verify_color_invariant (tree_elem *);

bool is_equal (int , int);

#endif

