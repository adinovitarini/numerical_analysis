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
* Sehingga, **$b_{i+1}=b_i+2c_ih_i+3d_ih_i^2$**.
### Step 6: Turunan kedua dari Persamaan $f_i(x)=a_i+b_i(x-x_i)+c_i(x-x_i)^2+d_i(x-x_i)^3$
* $$f_{i}^{''}(x_i) = 2c_{i}$$
* $$f_{i}^{''}(x) = 2c_i+6d_i(x_{i+1}-x_i)$$
### Step 7: Kondisi kontinuiti untuk turunan kedua
* $$f_{i+1}^{''}(x_{i+1}) = 2c_{i+1}$$
* $$f_{i}^{''}(x_{i+1}) = 2c_i+6d_i(x_{i+1}-x_i)$$
* $$f_{i}^{''}(x_{i+1}) = c_i+6d_ih_i$$
* Sehingga, **$c_{i+1}=c_i+3d_ih_i$**.
* Sehingga, **$d_{i+1}=\frac{c_{i+1}-c_i}{3h_i}$**.
### Step 8: Subtitusi $b_i$, $c_i$, dan $d_i$ ke Persamaan $y_{i+1} = y_i+b_i(x_{i+1}-x_i)+c_i(x_{i+1}-x_i)^2+d_i(x_{i+1}-x_i)^3$
$$y_{i+1} = y_i+b_ih_i+\frac{(2c_i+c_{i+1})h_i^2}{3}$$
### Step 9: Hitung nilai $b_i$ dari Step 8 
* $$b_i = \frac{y_{i+1}-y_i}{h_i}-\frac{(2c_i+c_{i+1})h_i^2}{3}$$
* Untuk bagian indeks sebelumnya menjadi $$b_{i-1} = \frac{y_{i}-y_{i-1}}{h_{i-1}}-\frac{(2c_{i-1}+c_{i})h_{i-1}^2}{3}$$
### Step 10: Substitusi nilai $d_i$ yang diperoleh dari Step 7 ke Persamaan **$b_{i+1}=b_i+2c_ih_i+3d_ih_i^2$** di Step 5
* $$b_{i+1}=b_i+2c_ih_i+(c_{i+1}-c_i)h_i$$
* Untuk bagian indeks sebelumnya menjadi $$b_{i}=b_{i-1}+2c_{i-1}h_{i-1}+(c_{i}-c_{i-1})h_{i-1}$$
### Step 11: Substitusi nilai $b_i$ dan $b_{i-1}$ yang diperoleh dari Step 9 ke Persamaan $b_{i}=b_{i-1}+2c_{i-1}h_{i-1}+(c_{i}-c_{i-1})h_{i-1}$
$$\frac{y_{i+1}-y_i}{h_i}-\frac{(2c_i+c_{i+1})h_i}{3}=\frac{y_i-y_{i-1}}{h_{i-1}}-\frac{(2c_{i-1}+c_i)h_{i-1}}{3}+(c_{i-1}+c_i)h_{i-1}$$
### Step 12: Kelompokkan bagian y dan c
$$\frac{y_{i+1}-y_i}{h_i}-\frac{y_i-y_{i-1}}{h_{i-1}}= \frac{(2c_i+c_{i+1})h_i}{3}-\frac{(2c_{i-1}+c_i)h_{i-1}}{3}+(c_{i-1}+c_i)h_{i-1}$$
### Step 13: Sederhanakan Persamaan yang diperoleh pada Step 12 dengan mengkalikannya dengan 3
* $$\frac{3(y_{i+1}-y_i)}{h_i}-\frac{3(y_i-y_{i-1})}{h_{i-1}}= (2c_i+c_{i+1})h_i-(2c_{i-1}+c_i)h_{i-1}+3(c_{i-1}+c_i)h_{i-1}$$
* $$h_{i-1}c_{i-1}+2(h_i-h_{i-1})c_i+h_ic_{i+1}=\frac{3(y_{i+1}-y_i)}{h_i}-\frac{3(y_i-y_{i-1})}{h_{i-1}}$$
### Step 14: Nyatakan Step 13 ke dalam bentuk matriks sbb
$$
\begin{bmatrix}
h_1 & 2(h_1 + h_2) & h_2 & 0 & \cdots \\
0 & h_2 & 2(h_2 + h_3) & h_3 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{bmatrix}
\cdot
\begin{bmatrix}
c_1 \\
c_2 \\
\vdots \\
c_{n-1} \\
c_n
\end{bmatrix}=
\begin{bmatrix}
\text{RHS}_1 \\
\text{RHS}_2 \\
\vdots \\
\text{RHS}_{n-1} \\
c_n
\end{bmatrix}
$$



