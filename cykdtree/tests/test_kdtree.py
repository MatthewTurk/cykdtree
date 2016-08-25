import numpy as np
from nose.tools import assert_equal
from nose.tools import assert_raises

import cykdtree

N = 100 ; leafsize = 10
pts2 = np.random.rand(N,2).astype('float64')
left_edge2 = np.zeros(2, 'float64')
right_edge2 = np.ones(2, 'float64')
pts3 = np.random.rand(N,3).astype('float64')
left_edge3 = np.zeros(3, 'float64')
right_edge3 = np.ones(3, 'float64')

def test_Leaf():
    leaf2 = cykdtree.Leaf(0, np.arange(N), left_edge2, right_edge2)
    leaf3 = cykdtree.Leaf(0, np.arange(N), left_edge3, right_edge3)

def test_PyKDTree():
    tree2 = cykdtree.PyKDTree(pts2, left_edge2, right_edge2, leafsize=leafsize)
    tree3 = cykdtree.PyKDTree(pts3, left_edge3, right_edge3, leafsize=leafsize)
    tree2 = cykdtree.PyKDTree(pts2, left_edge2, right_edge2, 
                              leafsize=leafsize, periodic=True)
    tree3 = cykdtree.PyKDTree(pts3, left_edge3, right_edge3, 
                              leafsize=leafsize, periodic=True)
    
def test_search():
    # 2D
    tree2 = cykdtree.PyKDTree(pts2, left_edge2, right_edge2, leafsize=leafsize)
    for pos in [left_edge2, (left_edge2+right_edge2)/2.]:
        leaf2 = tree2.get(pos)
    assert_raises(ValueError, tree2.get, right_edge2)
    # 3D
    tree3 = cykdtree.PyKDTree(pts3, left_edge3, right_edge3, leafsize=leafsize)
    for pos in [left_edge3, (left_edge3+right_edge3)/2.]:
        leaf3 = tree3.get(pos)
    assert_raises(ValueError, tree3.get, right_edge3)

def test_kdtree():
    leaves2 = cykdtree.kdtree(pts2, left_edge2, right_edge2, leafsize)
    leaves3 = cykdtree.kdtree(pts3, left_edge3, right_edge3, leafsize)
    assert_raises(ValueError, cykdtree.kdtree, pts2, left_edge2, right_edge2, 1)

def test_leaves():
    leaves2 = cykdtree.leaves('kdtree', pts2, left_edge2, right_edge2, False, leafsize)
    leaves3 = cykdtree.leaves('kdtree', pts3, left_edge3, right_edge3, False, leafsize)
    assert_raises(ValueError, cykdtree.leaves, 'invalid', pts2, left_edge2, right_edge2, False)
    # TODO: Value testing of leaf neighbors
    # assert_raises(NotImplementedError, cykdtree.leaves, 
    #               'kdtree', pts2, left_edge2, right_edge2, True, leafsize)
    # assert_raises(NotImplementedError, cykdtree.leaves, 
    #               'kdtree', pts3, left_edge3, right_edge3, True, leafsize)