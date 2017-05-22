   bool checkBST(Node* root) {
      bool left=false;		//is left subtree a bst?
      bool right = false;	//is right subtree a bst?
      if(root == NULL)		//base case: if tree is null, return true (a null tree is a bst).
          return true;
       
       if(allLessThan(root-> left,root->data))		//if all nodes in left subtree have data less than that of root
            left = checkBST(root->left);		//if so, check if left subtree is a bst
       else
            return false;				//otherwise this isn't a bst
     
       if(allGreaterThan(root -> right,root->data))	//if all nodes in right subtree have data more than that of root
              right = checkBST(root -> right);		//if so, check if right subtree is a bst
       else
              return false;				//otherwise this isn't a bst
      
      if(right && left)		//if both subtrees are bst's, this is a bst.
          return true;
      return false;
   }

   //returns true if all data within the tree of the root are less than d
   bool allGreaterThan(Node *root, int d){
       if(root == NULL)		//base case: if root is null, return true
           return true;
       if(root -> data <= d)	//if root's data is >d, return false
           return false;
       if(!allGreaterThan(root -> left,d) || !allGreaterThan(root -> right,d))		//if either subtree doesn't have data only less than d, return false
           return false;
       return true;		//if it gets to here, all data is less
   }

   //same as above, except checks if all data in root are greater than d
   bool allLessThan(Node *root, int d){
       if(root == NULL)
           return true;
       if(root -> data >= d)
           return false;
       if(!allLessThan(root -> left,d) || !allLessThan(root -> right,d))
           return false;
       return true;
   }