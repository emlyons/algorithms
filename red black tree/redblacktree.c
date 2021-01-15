#include "redblacktree.h"

/* Must be called before any other functions on a struct tree. */
void rb_init (tree *T, get_key_func f)
{
  T->nil.color = black;
  T->nil.parent = &T->nil;
  T->root = &T->nil;
  T->get_key = f;
}

/* Returns the key value of the given element */
int get_elem_key (tree *T, tree_elem *z)
{
  return T->get_key(z);
}

/* Standard binary tree left rotate algorithm */
void
tree_left_rotate (tree *T, tree_elem *x)
{
  tree_elem *y = x->right;

  x->right = y->left;
  if (y->left != &T->nil)
  {
    y->left->parent = x;
  }
  y->parent = x->parent;
  if (x->parent == &T->nil)
  {
    T->root = y;
  }
  else if (x == x->parent->left)
  {
    x->parent->left = y;
  }
  else
  {
    x->parent->right = y;
  }
  y->left = x;
  x->parent = y;
}

/* Standard binary tree right rotate algorithm */
void
tree_right_rotate (tree *T, tree_elem *y)
{
  tree_elem *x = y->left;
  y->left = x->right;
  if (x->right != &T->nil)
  {
    x->right->parent = y;
  }
  x->parent = y->parent;
  if (y->parent == &T->nil)
  {
    T->root = x;
  }
  else if (y == y->parent->right)
  {
    y->parent->right = x;
  }
  else
  {
    y->parent->left = x;
  }
  x->right = y;
  y->parent = x;
}

/* Replaces node u with node v. */
void
rb_transplant (tree *T, tree_elem *u, tree_elem *v)
{
  if (u->parent == &T->nil)
  {
    T->root = v;
  }
  else if (u == u->parent->left)
  {
    u->parent->left = v;
  }
  else
  {
    u->parent->right = v;
  }
  v->parent = u->parent;
}

/* Fixes broken red black properties that may be violated when inserting a new node. Recall inserted nodes are always red.
 case 1: The new node's parent and the parents sibling are also red. The new node and it's parent are the same direction descendents.
 case 2: The new node's parent is red, the parent's sibling is black. The new node and it's parent are opposite direction descendants.
 case 3: The new node's parent is red, the parent's sibling is black. The new node and it's parent are the same direction descendants. */
void
rb_insert_fixup (tree *T, tree_elem *z)
{
  tree_elem *y;
  
  while (z->parent->color == red)
  {

    /* z's parent is a left child */
    if (z->parent == z->parent->parent->left)
    {
      y = z->parent->parent->right;
      /* case 1 */
      if (y->color == red)
      {
	z->parent->color = black;
	y->color = black;
	z->parent->parent->color = red;
	z = z->parent->parent;
      }
      /* case 2 */
      else if (z == z->parent->right)
      {
	z = z->parent;
	tree_left_rotate(T,z);
      }
      /* case 3 */
      else
      {
	z->parent->color = black;
	z->parent->parent->color = red;
	tree_right_rotate(T, z->parent->parent);
      }
    }

    /* z's parent is a right child */
    else if (z->parent == z->parent->parent->right)
    {
      y = z->parent->parent->left;
      /* case 1 */
      if (y->color == red)
      {
	z->parent->color = black;
	y->color = black;
	z->parent->parent->color = red;
	z = z->parent->parent;
      }
      /* case 2 */
      else if (z == z->parent->left)
      {
	z = z->parent;
	tree_right_rotate(T,z);
      }
      /* case 3 */
      else
      {
	z->parent->color = black;
	z->parent->parent->color = red;
	tree_left_rotate(T, z->parent->parent);
      }
    }
 
  }
  T->root->color = black;
}

/* Maintains red black properties that may be violated after deleting a node. */
void rb_delete_fixup (tree *T, tree_elem *x)
{
  tree_elem *w;
  
  while (x != T->root && x->color == black)
  {
    
    if (x == x->parent->left)
    {
      w = x->parent->right;
      if (w->color == red)
      {
	w->color = black;
	x->parent->color = red;
	tree_left_rotate(T, x->parent);
	w = x->parent->right;
      }
      if (w->left->color == black && w->right->color == black)
      {
	w->color = red;
	x = x->parent;
      }
      else if (w->right->color == black)
      {
	w->left->color = black;
	w->color = red;
	tree_right_rotate(T, w);
	w = x->parent->right;
      }
      else
      {
	w->color = x->parent->color;
	x->parent->color = black;
	w->right->color = black;
	tree_left_rotate(T, x->parent);
	x = T->root;
      }
    }

    else if (x == x->parent->right)
    {
      w = x->parent->left;
      if (w->color == red)
      {
	w->color = black;
	x->parent->color = red;
	tree_right_rotate(T, x->parent);
	w = x->parent->left;
      }
      if (w->right->color == black && w->left->color == black)
      {
	w->color = red;
	x = x->parent;
      }
      else if (w->left->color == black)
      {
	w->right->color = black;
	w->color = red;
	tree_left_rotate(T, w);
	w = x->parent->left;
      }
      else
      {
	w->color = x->parent->color;
	x->parent->color = black;
	w->left->color = black;
	tree_right_rotate(T, x->parent);
	x = T->root;
      }
    }
    
  }
  x->color = black;
}

/* Inserts a new node. runs in O(log N) */
void
rb_insert (tree *T, tree_elem *z)
{  
  tree_elem *x = T->root;
  tree_elem *y = &T->nil;
    
  while (x != &T->nil)
  {
    y = x;
    if (T->get_key(z) <= T->get_key(x))
    {
      x = x->left;
    }
    else
    {
      x = x->right;
    }
  }
  z->parent = y;
  if (y == &T->nil)
  {
    T->root = z;
  }
  else if (T->get_key(z) <= T->get_key(y))
  {
    y->left = z;
  }
  else
  {
    y->right = z;
  }
  z->left = &T->nil;
  z->right = &T->nil;
  z->color = red;
  rb_insert_fixup(T, z);
}

/* Removes an existing node. runs in O(log N) */
void
rb_delete (tree *T, tree_elem *z)
{
  tree_elem *x;
  tree_elem *y = z;
  node_color y_original_color = y->color;
  
  if (z->left == &T->nil)
  {
    x = z->right;
    rb_transplant(T, z, z->right);
  }
  else if (z->right == &T->nil)
  {
    x = z->left;
    rb_transplant(T, z, z->left);
  }
  else
  {
    y = tree_minimum(T, z->right);
    y_original_color = y->color;
    x = y->right;
    if (y->parent == z)
    {
      x->parent = y;
    }
    else
    {
      rb_transplant(T, y, y->right);
      y->right = z->right;
      y->right->parent = y;
    }
    rb_transplant(T, z, y);
    y->left = z->left;
    y->left->parent = y;
    y->color = z->color;
  }
  if (y_original_color == black)
  {
    rb_delete_fixup(T, x); 
  }
}

/* Returns the maximum key node in the subtree rooted at the given node. If called on the root node gives the minimum of the entire tree. runs in O(log N) */
tree_elem *tree_maximum (tree *T, tree_elem *z)
{
  tree_elem *x = z;
  tree_elem *y = &T->nil;

  while (x != &T->nil)
  {
    y = x;
    x = x->right;
  }
  return y;
}

/* Returns the minimum key node in the subtree rooted at the given node. If called on the root node gives the maximum of the entire tree. runs in O(log N) */
tree_elem *tree_minimum (tree *T, tree_elem *z)
{
  tree_elem *x = z;
  tree_elem *y = &T->nil;

  while (x != &T->nil)
  {
    y = x;
    x = x->left;
  }
  return y;
}




/* testing */

int invariant_black_count;

/* tests tree 'T' for any red black tree invariant violations. returns true if all invariants are satisfied */
bool rb_verify_tree (tree *T)
{
  invariant_black_count = 0;

  if (!rb_verify_root_invariant (T))
    return false;

  if (!rb_verify_leaf_invariant (T))
    return false;

  /* invariants on all nodes */
  if (T->root != &T->nil)
  {
    return rb_verify_node (T, T->root, 0);
  }

  /* empty tree */
  return true;
}

/* Traverses each node in the red black tree and verifies the associated invariants described in the proceeding functions */
bool rb_verify_node (tree *T, tree_elem *e, int black_count)
{ 
  if (!rb_verify_color_invariant (e))
    return false;
  
  /* black node */
  if (e->color == black)
    black_count++;

  /* red node */
  if (e->color == red)
    if (!rb_verify_child_invariant (T, e))
      return false;

  /* leaf node */
  if (e->left == &T-> nil && e->right == &T->nil)
    return rb_verify_path_invariant (black_count);

  /* left child */
  if (e->left != &T->nil)
    if (!rb_verify_node (T, e->left, black_count))
      return false;
  
  /* right child */
  if (e->right != &T->nil)
    if (!rb_verify_node (T, e->right, black_count))
      return false;

  return true;
}

/* verify the red black path invariant at a leaf node. all paths in a red black tree must have the same number of black nodes. */
bool rb_verify_path_invariant (int black_count)
{
  if (invariant_black_count == 0)
  {
    invariant_black_count = black_count;
    return true;
  }
  else
  {
    return is_equal (invariant_black_count, black_count);
  }
}

/* verify the red black parent/child invariant on a node. any child of a red node must be black. */
bool rb_verify_child_invariant (tree *T, tree_elem *e)
{
  if (e->color == red)
  {
    if (e->left != &T->nil && e->left->color == red)
      return false;
    else if (e->right != &T->nil && e->right->color == red)
      return false;
    else
      return true;
  }
}

/* verify the red black tree root invariant. the root node must always be black */
bool rb_verify_root_invariant (tree *T)
{
  if (T->root->color != black)
    return false;
  return true;
}

/* verify thre red black tree leaf invariant. leaf (nil) node must be black. */
bool rb_verify_leaf_invariant (tree *T)
{
  if (T->nil.color != black)
    return false;
  return true;
}

/* verify the red black tree color invariant. all nodes must be either red or black */
bool rb_verify_color_invariant (tree_elem *e)
{
  if (e->color == black || e->color == red)
    return true;
  else
    return false;
}

/* equality check - useful to have in seperate function for readability during debugging */
bool is_equal (int a, int b)
{
  if (a == b)
    return true;
  else
    return false;
}
