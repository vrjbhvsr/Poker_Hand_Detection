import os
import logging
from datetime import datetime
from from_root import from_root

now = datetime.now()

filename = f"{now.strftime('%Y-%m-%d-%H-%M')}.log"

log_path = os.path.join(from_root(),"logs",filename)

os.makedirs(log_path, exist_ok=True)

log_file = os.path.join(log_path,filename)

logging.basicConfig(filename=log_file,level=logging.INFO,format= '[%(asctime)s] %(name)s %(levelname)s:- %(message)s')
