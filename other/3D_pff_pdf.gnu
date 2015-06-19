set term post eps enhanced color font "Times-Roman,30"
set border linewidth 3
set output "Pff_2.eps"
set xlabel "{/Times-Italic f_n/<f_n>}" font ",30"
set ylabel "{/Times-Italic f_t/<f_t>}" font ",30"
unset key
set pm3d
set palette rgbformulae 22,13,-31
set size square
set view map
set xtics 1
set ytics 1
set cbtics 0.1
set xrange [0:4]
set yrange [0:4]
set log cb
set cbrange [0.01:]
set cbtics 0.01,2,0.5
set cbtics add (" 0.48" 0.48)
splot "3D.txt" w pm3d
