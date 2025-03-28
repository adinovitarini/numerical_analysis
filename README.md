# Penurunan Rumus Cubic Splines 
Persamaan fungsi cubic splines dapat dinyatakan ke dalam Persamaan $f_i(x)=a_i+b_i(x-x_i)+c_i(x-x_i)^2+d_i(x-x_i)^3$
### Step 1: Hitung $f_i(x_i)$
$$f_i(x_i) = a_i+b_i(x_i-x_i)+c_i(x_i-x_i)^2+d_i(x_i-x_i)^3$$
$$f_i(x_i) = a_i$$
Oleh karena itu, $a_i$ dapat dinyatakan sebagai 
$$a_i = y_i$$
### Step 2: Hitung jarak antar titik interpolasi 
$$h_i = x_{i+1}-x_i$$
### Step 3: Definisikan kondisi kontinuiti antar spline 
* Untuk Left Handes Splines (LHS) $f_{i+1}(x_{i+1})$
* $f_{i+1}(x_{i+1})$
* $f_{i+1}(x_{i+1})$
