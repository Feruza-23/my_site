body {
    background: linear-gradient(45deg, #9890e3, #b1f4cf);
    margin-left: auto;
    margin-right: auto;
}

@keyframes color-change {
    0% {
      color: blue;
    }
  
    50% {
      color: red;
    }
  
    100% {
      color: blue;
    }
}

h1 {
    color: rgb(16, 48, 16);
    text-align: center;
    border: 5px solid rgb(255, 255, 255);
    border-radius: 10px;
}
h1:hover{
    animation: color-change 3s infinite;
    color:rgb(7, 22, 7);
}
h2 {
    color: rgb(46, 5, 83);
}
p {
    font-family: Arial, Helvetica, sans-serif;
    color: rgb(27, 27, 36);
    text-align: center;
    border: 5px solid rgba(190, 24, 24, 0.527);
}
b {
    color: rgb(68, 11, 49);
    font-size: 24px;
}
strong {
    color: rgb(4, 37, 41);
    font-size: 24px;
}
img {
    width: 500px;
}
h4 {
    color: black;
}
h3 {
    color: rgb(29, 8, 49);
}
