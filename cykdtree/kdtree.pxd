cimport numpy as np
from libcpp.vector cimport vector
from libcpp.pair cimport pair
from libcpp cimport bool
from libc.stdint cimport uint32_t, uint64_t, int64_t, int32_t

cdef extern from "c_kdtree.hpp":
    cdef cppclass Node:
        bool is_leaf
        uint32_t leafid
        uint32_t ndim
        vector[double] left_edge
        vector[double] right_edge
        uint64_t left_idx
        uint64_t children
        uint32_t split_dim
        double split
        Node* less
        Node* greater
        vector[bool] periodic_left
        vector[bool] periodic_right
        vector[vector[uint32_t]] left_neighbors
        vector[vector[uint32_t]] right_neighbors
    cdef cppclass KDTree:
        double* all_pts
        uint64_t* all_idx
        uint64_t npts
        uint32_t ndim
        uint32_t leafsize
        double* domain_left_edge
        double* domain_right_edge
        double* domain_mins
        double* domain_maxs
        vector[Node*] leaves
        Node* root
        KDTree(double *pts, uint64_t *idx, uint64_t n, uint32_t m, uint32_t leafsize0,
               double *left_edge, double *right_edge)
        KDTree(double *pts, uint64_t *idx, uint64_t n, uint32_t m, uint32_t leafsize0,
               double *left_edge, double *right_edge, bool periodic)
        Node* search(double* pos)

cdef class PyKDTree:
    cdef KDTree *_tree
    cdef readonly uint64_t npts
    cdef readonly uint32_t ndim
    cdef readonly uint32_t num_leaves
    cdef readonly uint32_t leafsize
    cdef readonly object leaves
    cdef readonly object idx
    cdef readonly object left_edge
    cdef readonly object right_edge
    cdef readonly object domain_width
    cdef readonly bool periodic
