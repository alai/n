#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SN4S ver 0.1

import io
post_info_tags = ['date: ', 'url: ']
def readMd(fn):
    # Read single markdown file and get all contents extracted
    file_opr = io.open(fn,'r',encoding='utf-8')
    file_content = file_opr.readlines()
    file_content = [l.replace('\n','') for l in file_content if l.replace('\n','') != ''] #remove linewrap and empty lines
        # get all titles, including the post title
    titles = [l for l in file_content if l.startswith('#')]
        # assign contents under the title they belongs to
    post_dict = {}
    post_dict['post_info'] = []
    root = titles[0] # use the head title as root key for if there is no sub-level title in the begining
    post_dict[root] = []
    for l in file_content:
        if l.startswith('# '):# the head title level-0 
            post_dict['post_title'] = l
        else:
            if any(l.startswith(pi_tag) for pi_tag in post_info_tags): #post info snippets
                post_dict['post_info'].append(l)
            elif l.startswith('##'): # level-1 title
                current_title = l
                post_dict[current_title] = []
            else:
                post_dict[current_title].append(l)
    return post_dict,titles

def printPost(post_dict,titles):
    # Print post in terminal for testing
    for tag in post_dict['post_info']:
        print(tag)
    for k in titles:
        print('\n'+k)
        for p in post_dict[k]:
            print('\t'+p)


if __name__ == "__main__":
    md_file = "./Compass.md"
    fc,titles = readMd(md_file)
    printPost(fc,titles)
