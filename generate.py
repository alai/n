#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SN4S ver 0.1

import io
import os
import jinja2

post_info_tags = ['date: ', 'url: ']

def titleListToDict(titles):
    title_dict = {}
    for i in range(len(titles)):
        title_seq = 'title'+str(i)
        title_dict[titles[i]] = title_seq
    return title_dict

def readMd(fn):
    # Read single markdown file and get all contents extracted and returns:
    # put all extracted data into the post_data for rendering in the template
    #   - post_data['titles']       all titiles in sequence
    #   - post_data['post_info']    post info tags like, data, url, etc
    #   - post_data['title_id']     title to it id 'title(n)'
    #   - post_data['post_title']   the post title (title0)

    file_opr = io.open(fn,'r',encoding='utf-8')
    file_content = file_opr.readlines()
    file_content = [l.replace('\n','') for l in file_content if l.replace('\n','') != ''] #remove linewrap and empty lines
        # get all titles, including the post title
    titles = [l for l in file_content if l.startswith('#')]
    clean_titles = [t.replace('#','').strip() for t in titles]
    title_id = titleListToDict(clean_titles)
        # assign contents under the title they belongs to
    post_data = {}
    post_data['title_id'] = title_id
    post_data['titles'] = [t.replace('#','').strip() for t in titles] #remove # from titles for HTML display
    post_data['post_info'] = []
    post_data['title0'] = []
    for l in file_content:
        if l.startswith('# '):# the head title level-0 
            post_data['post_title'] = l.replace('#','').strip()
        else:
            if any(l.startswith(pi_tag) for pi_tag in post_info_tags): #post info snippets
                post_data['post_info'].append(l)
            elif l.startswith('##'): # level-1 title
                current_title = 'title'+str(titles.index(l))
                post_data[current_title] = []
            else:
                post_data[current_title].append(l)
    return post_data

def printPost(post_data,titles):
    # Print post in terminal for testing
    for tag in post_data['post_info']:
        print(tag)
    for k in titles:
        seq = titles.index(k)
        title_seq = 'title'+str(seq)
        print('\n'+k+' '+title_seq)
        for p in post_data[title_seq]:
            print('\t'+p)

def renderPage(fn_temp,post):
    # Print (render) the post into html
    jinja_template = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))
    template = jinja_template.get_template(fn_temp)
    page = template.render(post=post_d)
    return page

def writeHTML(page,fn_html):
    # write rendered page as html
    html_opr = open(fn_html,'w')
    html_opr.write(page)
    html_opr.close()
    print('%s saved.'%fn_html)
    return

if __name__ == "__main__":
    md_file = "./Compass.md"
    post_d = readMd(md_file)
    #printPost(post_d,titles)
    page = renderPage('./s_template.html',post_d)
    print(page)
    writeHTML(page,'compass.html')

