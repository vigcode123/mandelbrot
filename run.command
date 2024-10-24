if ! test -d ./venv ; then                                                      
  echo "venv does not exist. making new one"                                    
  python3 -m venv venv    
  source venv/bin/activate                                               
fi  

python3 mandelbrot.py
