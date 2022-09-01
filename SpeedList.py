import string
import time
import random
import concurrent.futures
import re,
import math
import hashlib
    

class SpeedList:
    
    def __init__(self):
        
        self.made = True
        self.letters_numbers = string.ascii_lowercase + string.digits
                
    def make_dummy(self, n_chars, n_items):
                
        return [''.join([random.choice([x for x in self.letters_numbers]) for _ in range(n_chars)]) for _ in range(n_items)]
            
                
    def make_hydra(self, use=None):
        
        """
        Define spawn class
        
        """
        
        class spawn:
            
            def __init__(self):
                
                import string, uuid
                
                self.hydra = {}
                self.letters_numbers = string.ascii_lowercase + string.digits
                _ = [self.hydra.update({x:[]}) for x in self.letters_numbers]
                self.salt =  uuid.uuid4().hex

            def chunk_set(self, lst, n):

                for i in range(0, len(lst), n):
                    yield set(lst[i:i + n])
                    
            def make_from(self, in_list):
                
                if type(in_list) == 'set':
                    in_list = list(in_list)
                
                _ = [self.hydra.update({x:[]}) for x in self.letters_numbers]
                new_hydra = [self.hydra[hashlib.md5(item.encode('utf-8')).hexdigest()[0].lower()].append(item) for item in in_list]
                
                return new_hydra
            
            
            def append(self, item):
                
                first = hashlib.md5(item.encode('utf-8')).hexdigest().lower()[0]
                
                self.hydra[first].append(item)
                
                return


            def extend(self, in_list):
                
                for item in in_list:   
         
                    first = hashlib.md5(item.encode('utf-8')).hexdigest().lower()[0]
                    self.hydra[first].append(item)
                
                return
            
                
            def remove(self, items):
              
                if type(items) == 'str':
                    items = [items]
                  
                for item in items:
                    
                    first = hashlib.md5(item.encode('utf-8')).hexdigest().lower()[0]
                    
                    try:
                        self.hydra[first].remove(item)
                    except ValueError:
                        continue
                    
                return
            
            
            def index(self, search_for, num=True):

                first = hashlib.md5(search_for.encode('utf-8')).hexdigest().lower()[0]
                    
                if search_for in self.hydra[first]:
                    
                    return (first, self.hydra[first].index(search_for))
                
                else:
                    return None
                
                
            def see(self, search_for, threads=0):
                
                first = hashlib.md5(search_for.encode('utf-8')).hexdigest().lower()[0]
            
                if len(self.hydra[first]) > 500:
                    chunk_count = math.floor(len(self.hydra[first])/500)
                    hydra_sets = list(self.chunk_set(self.hydra[first], chunk_count))
                    
                    if not threads:
                        for each_set in hydra_sets:
                            if search_for in each_set:
                                return True
                        
                        return False
                    
                    else:
                        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                            futures = [executor.submit(self.check_if_in, chunk, search_for) for chunk in hydra_sets]
                            
                            for future in concurrent.futures.as_completed(futures):
                                if future.result() == True:
                                    return True
                        return False
                    
                elif search_for in self.hydra[first]:
                    return True
                
                else:
                    return False


            def check_if_in(self, chunk, search_for):
                
                if search_for in chunk:
                    return True
                
                else:
                    return False
            
            def merge(self, new_hydra):
                
                merged = [self.hydra[x[0].lower()].append(x) if not re.search('(^[^\w\d])', x) \
                          else self.hydra[str(abs(hash(x)))[0]].append(x) for x in new_hydra.values()]
                
                merged = [self.hydra[
                
                return merged
            
            
            def dump(self, to_list=True, to_set=False, to_dict=False, to_string=False):
                
                dump_list = [x for x in self.hydra.values() if x]
                
                if to_string:
                    return ' '.join(dump_list)
                
                if to_set:
                    return set(dump_list)
                
                if to_dict:
                    return self.hydra
                
                if to_list:
                    return dump_list
                
            
            def dedupe(self):
                
                for branch in self.letters_numbers:
                    
                    hold = []
                    
                    _ = [hold.append(e) for e in self.hydra[branch] if e not in hold]
                    
                    self.hydra[branch] = hold.copy()
                
                return
                
        hydra = spawn()
        
        hydra.make_from(use)
        
        return hydra
    