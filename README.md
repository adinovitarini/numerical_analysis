# Penurunan Rumus Cubic Splines 
Persamaan fungsi cubic splines dapat dinyatakan ke dalam Persamaan $f_i(x)=a_i+b_i(x-x_i)+c_i(x-x_i)^2+d_i(x-x_i)^3$
### Step 1: Hitung $f_i(x_i)$
$$f_i(x_i) = a_i+b_i(x_i-x_i)+c_i(x_i-x_i)^2+d_i(x_i-x_i)^3$$
$$f_i(x_i) = a_i$$
Oleh karena itu, $a_i$ dapat dinyatakan sebagai 
$$a_i = y_i$$
### Step 2: Hitung jarak antar titik interpolasi 
$$h_i = x_{i+1}-x_i$$
### Step 3: Definisikan kondisi kontinuiti antar spline $f_{i+1}(x_{i+1}) = f_i(x_{i+1})$
* Untuk Left Handed Splines (LHS): $f_{i+1}(x_{i+1}) = y_{i+1}$
* Untuk Right Handed Splines (RHS): $f_{i}(x_{i+1})=a_i+b_i(x_{i+1}-x_i)+c_i(x_{i+1}-x_i)^2+d_i(x_{i+1}-x_i)^3$
* Substitusi LHS dan RHS ke $f_{i+1}(x_{i+1}) = f_i(x_{i+1})$ sedemikian hingga menjadi $y_{i+1} = y_i+b_i(x_{i+1}-x_i)+c_i(x_{i+1}-x_i)^2+d_i(x_{i+1}-x_i)^3$
* Sederhanakan persamaan di atas sehingga menjadi $y_{i+1} = y_i+b_ih_i+c_ih_i^2+d_ih_i^3$
### Step 4: Turunan pertama dari Persamaan $f_i(x)=a_i+b_i(x-x_i)+c_i(x-x_i)^2+d_i(x-x_i)^3$
* $$f_{i}^{'}(x_i) = b_{i}$$
* $$f_{i}^{'}(x) = b_i+2c_i(x_{i+1}-xi)+3d_i(x_{i+1}-x_i)^2$$
### Step 5: Kondisi kontinuiti untuk turunan pertama 
* $$f_{i+1}^{'}(x_{i+1}) = b_{i+1}$$
* $$f_{i}^{'}(x_{i+1}) = b_i+2c_i(x_{i+1}-xi)+3d_i(x_{i+1}-x_i)^2$$
* $$f_{i}^{'}(x_{i+1}) = b_i+2c_ih_i+3d_ih_i^2$$
### Step 6: Turunan kedua dari Persamaan $f_i(x)=a_i+b_i(x-x_i)+c_i(x-x_i)^2+d_i(x-x_i)^3$
* $$f_{i}^{''}(x_i) = 2c_{i}$$
* $$f_{i}^{''}(x) = 2c_i+6d_i(x_{i+1}-x_i)$$
### Step 7: Kondisi kontinuiti untuk turunan kedua
* $$f_{i+1}^{''}(x_{i+1}) = 2c_{i}$$
* $$f_{i}^{''}(x_{i+1}) = b_i+2c_i(x_{i+1}-xi)+3d_i(x_{i+1}-x_i)^2$$
* $$f_{i}^{''}(x_{i+1}) = b_i+2c_ih_i+3d_ih_i^2$$
