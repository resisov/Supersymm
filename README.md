# Supersymm

Simple SUSY (MSSM) event generation

- mg5 command

Scalar top pair generation

```bash
./mg5_aMC
>>import model MSSM_UFO
>>generate p p > t1 t1~
```

1. Stop to top and neutralino
2. dileptonic decay of top pair

- madspin command
```bash
>>decay t1 > t n1, t > w+ b, w+ > l+ vl
>>decay t1~ > t~ n1, t~ > w- b~, w- > l- vl~
```
