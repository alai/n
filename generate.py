#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SN4S ver 0.1

import io

post_info_tags = ['date: ', 'url: ']
def readMd(fn):
    # Read single markdown file and get all contents extracted and returns:
    ## post_dict - {title:[paras]}
    ##           - post_dict['post_info']: post infomartion tags
    ## titles    - [title]
    file_opr = io.open(fn,'r',encoding='utf-8')
    file_content = file_opr.readlines()
    file_content = [l.replace('\n','') for l in file_content if l.replace('\n','') != ''] #remove linewrap and empty lines
        # get all titles, including the post title
    titles = [l for l in file_content if l.startswith('#')]
        # assign contents under the title they belongs to
    post_dict = {}
    post_dict['post_info'] = []
    post_dict['title0'] = []
    for l in file_content:
        if l.startswith('# '):# the head title level-0 
            post_dict['post_title'] = l
        else:
            if any(l.startswith(pi_tag) for pi_tag in post_info_tags): #post info snippets
                post_dict['post_info'].append(l)
            elif l.startswith('##'): # level-1 title
                current_title = 'title'+str(titles.index(l))
                post_dict[current_title] = []
            else:
                post_dict[current_title].append(l)
    return post_dict,titles

def printPost(post_dict,titles):
    # Print post in terminal for testing
    for tag in post_dict['post_info']:
        print(tag)
    for k in titles:
        seq = titles.index(k)
        title_seq = 'title'+str(seq)
        print('\n'+k+' '+title_seq)
        for p in post_dict[title_seq]:
            print('\t'+p)


if __name__ == "__main__":
    md_file = "./Compass.md"
    fc,titles = readMd(md_file)
    printPost(fc,titles)
