
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import datetime

def std_occ(title): 
    '''Inputs the occupation title of the contributor and organizes it into supercategories
    '''
    
    if isinstance(title, float):
        return None
    t = title.lower().strip().split()
    
    for word in ['retired']:
        if word in t: 
            title = 'retired'
            break
            
    for word in ['attorney', 'lawyer', 'general counsel', 'judge','clerk', 'investigator','officer','paralegal']:
        if word in t:
            title = 'law'
            break
            
    for word in ['teacher','professor', 'educator', 'student', 'instructor','prof','librarian','education','tutor']:
        if word in t:
            title = 'education'
            break
            
    for word in ['physician','doc','r.n.','surgeon','nurse','psychologist','therapist']:
        if word in t: 
            title = 'healthcare'
            break
            
    for word in ['trade','government', 'federal', 'fed','policy', 'consultant','consulting', 'program', 'manager', 'analyst', 'diplomat', 'organizer','public']:
        if word in t:
            title = 'business/gov'
            break
            
    for word in ['executive', 'ceo', 'chief', 'director','president','vice', 'owner','partner','management','vp', 'finance','senior']: 
        if word in t:
            title = 'leadership'
            break
   
    for word in ['economics','economic', 'economist', 'researcher','research','scientist']:
        if word in t: 
            title = 'science'
            break       
    
    for word in ['not', 'information', 'requested','homemaker']:
        if word in t: 
            title = 'not employed or unknown'
            break   
            
    for word in ['cybersecurity', 'software', 'engineer', 'it', 'technology','web','technical']:
        if word in t:
            title ='it'
            break
            
    for word in ['writer', 'communications','editor','author','musician', 'designer','artist','art']:
        if word in t: 
            title = 'artist/comm'
            break
            
    for word in ['realtor', 'estate', 'architect','chst']:
        if word in t: 
            title = 'real estate/construction'
            break   
    
    for word in ['sales', 'retail', 'supervisor']:
        if word in t: 
            title = 'sales'
            break   
    if title not in ['not employed or unknown','law','business/gov','leadership','education','it','artist/comm','science','real estate/construction','healthcare','retired','sales']:
        title = 'other'
    return title.lower()


