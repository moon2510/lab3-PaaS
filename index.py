<!DOCTYPE html>
<html lang="en">

<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel="icon" href="favicon.ico" />
   <title>Hacker</title>
</head>
<style>
.wrapper {
   top: 50%;
   left: 50%;
   position: absolute;
   perspective: 1500px;
}

.box-area {
   position: absolute;
   animation-name: rotate;
   animation-duration: 20s;
   transform-style: preserve-3d;
   animation-timing-function: linear;
   animation-iteration-count: infinite;
}

@keyframes rotate {
   0% {
      transform: rotate3d(0, 0, 0, 0);
   }
   100% {
      transform: rotate3d(0, 1, 0, 360deg);
   }
}

.box {
   width: 300px;
   height: 300px;
   position: absolute;
   background-size: cover;
   border: 5px solid #0d1117;
   background-repeat: no-repeat;
}

.front-box {
   transform: translateX(-150px) translateY(-150px) translateZ(150px);
}

.front-middle-box {
   border: none;
   transform: translateX(-150px) translateY(-150px) translateZ(0px);
   background: url("https://lh3.googleusercontent.com/proxy/2uDQwr-nmbWDMbOkz3az7tBK406cPltkRQx33zdd6xxm1AyjboMZgABM8p6HvSaKWyTPH4Pb9lkiR8rS3zcjGHYcgiLWA9-p3N3fREssSY_mw1PH");
   background-size: 300px 300px;
}

.back-middle-box {
   border: none;
   transform: translateX(-150px) translateY(-150px) translateZ(0px) rotateY(-180deg);
   background: url("https://lh3.googleusercontent.com/proxy/2uDQwr-nmbWDMbOkz3az7tBK406cPltkRQx33zdd6xxm1AyjboMZgABM8p6HvSaKWyTPH4Pb9lkiR8rS3zcjGHYcgiLWA9-p3N3fREssSY_mw1PH");
   background-size: 300px 300px;
}

.back-box {
   transform: translateX(-150px) translateY(-150px) translateZ(-150px);
}

.right-box {
   transform: translateY(-150px) rotateY(90deg);
}

.left-box {
   transform: translateY(-150px) translateX(-300px) rotateY(90deg);
}

.bottom-box {
   transform: translateX(-150px) rotateX(90deg);
   background: #ffffff;
}

.top-box {
   background-color: #ffffff;
   transform: translateX(-150px) translateY(-300px) rotateX(90deg);
}

@media (min-width: 600px) {
   .box {
      width: 400px;
      height: 400px;
   }
   .front-box {
      transform: translateX(-200px) translateY(-200px) translateZ(200px);
   }
   .front-middle-box {
      transform: translateX(-200px) translateY(-200px) translateZ(0px);
   }
   .back-middle-box {
      transform: translateX(-200px) translateY(-200px) translateZ(0px) rotateY(-180deg);
   }
   .back-box {
      transform: translateX(-200px) translateY(-200px) translateZ(-200px);
   }
   .right-box {
      transform: translateY(-200px) rotateY(90deg);
   }
   .left-box {
      transform: translateY(-200px) translateX(-400px) rotateY(90deg);
   }
   .bottom-box {
      transform: translateX(-200px) rotateX(90deg);
   }
   .top-box {
      transform: translateX(-200px) translateY(-400px) rotateX(90deg);
   }
}

</style>
<body>
      <div class="wrapper">
         <div class="box-area">
            <div class="box front-box"></div>
            <div class="box front-middle-box"></div>
            <div class="box right-box"></div>
            <div class="box back-middle-box"></div>
            <div class="box back-box"></div>
            <div class="box left-box"></div>
            <div class="box top-box"></div>
            <div class="box bottom-box"></div>
         </div>
      </div>
      print("Hello World")
 </body>
</html>
