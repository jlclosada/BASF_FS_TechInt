<template>
    <div class="hero">
      <div class="overlay"></div>
      <div class="container">
        <div class="row">
          <div class="col-md-6 col-md-offset-6 col-xs-12">
            <nav>
              <div id="menu-toggle">
                <div class="hamburger">
                  <span class="line"></span>
                  <span class="line"></span>
                  <span class="line"></span>
                </div>
                <div class="cross">
                  <span class="line"></span>
                  <span class="line"></span>
                </div>
              </div>
            </nav>
            <div class="hero-text">
              <h1>Hi, I am<br>Jose Luis Cáceres</h1>
              <h3>Software Engineer</h3>
              <a href="/list" class="btn btn-lg btn-primary">To the exercise</a>
              <div class="container">
                <h4 class="sub-heading"></h4>
                <h4 class="hero-text"><span class="blue">Hope</span> you find my work interesting</h4>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <section class="stats">
      <div class="container">
        <div class="row">
          <div class="col-md-4 text-center stat-box">
            <h2 class="white">Degree in Mining Engineering</h2>
            <br><h2 class="white">Master in Environmental Sciences</h2>
            <br><img class="env" src="@/assets/env.png" alt="env" />
          </div>
          <div class="col-md-4 text-center stat-box">
            <h2 class="white">Tools</h2>
            <br><img class="python" src="@/assets/python.png" alt="python" />
            <br><img class="nuxt" src="@/assets/nuxt.png" alt="nuxt" />
            <br><img class="postgre" src="@/assets/postgre.png" alt="postgre" />
          </div>
          <div class="col-md-4 text-center stat-box">
            <h2 class="white">Experience</h2>
            <br><img class="bbva" src="@/assets/BBVA.png" alt="BBVA" />
            <br><img class="tragsa" src="@/assets/Tragsa.png" alt="tragsa" />
            <br><img class="inclam" src="@/assets/inclam.png" alt="inclam" />
          </div>
        </div>
      </div>
    </section>
  
    <section class="contact-banner">
      <div class="container">
        <div class="row">
          <div class="col-md-12 text-center">
            <h1>You can find me here!</h1>
            <a href="https://www.linkedin.com/in/jos%C3%A9-luis-c%C3%A1ceres-losada-0a0185125/" class="btn btn-lg btn-primary">Go to LinkedIN</a>
          </div>
        </div>
      </div>
    </section>
  
    <footer>
      <div class="container-fluid">
        <div class="row footer">
          <div class="col-md-12 text-center">
            <h1>Jose Luis Cáceres</h1>
            <h6>Interview for BASF</h6>
          </div>
        </div>
      </div>
    </footer>
  </template>
  
  <script setup>
  </script>
  
  <style scoped>
  .hero {
    background-image: url('/assets/wallpaper.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    position: relative;
    padding: 80px 0;
    text-align: center;
    color: white;
  }
  
  .hero .overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(5px); 
    z-index: 1;
  }
  
  .hero .hero-text {
    position: relative;
    z-index: 2;
    max-width: 600px;
    margin: 0 auto;
  }
  
  .hero-text h1 {
    font-size: 50px;
    font-weight: bold;
  }
  
  .hero-text h3 {
    font-size: 24px;
    color: #ddd;
  }
  
  .hero-text .btn {
    background-color: #3498db;
    color: white;
    padding: 12px 30px;
    margin-top: 20px;
    text-decoration: none;
  }
  
  .hero-text .btn:hover {
    background-color: #2980b9;
  }
  
  .bbva, .tragsa, .env, .inclam {
    width: 150px;
    height: auto;
  }

  .python, .postgre, .nuxt{
    width: 100px;
    height: auto;
    margin-top: 10px;
  }
  
  .case-study {
    padding: 60px 0;
    background-color: #f1f1f1;
    text-align: center;
  }
  
  .heading {
    font-size: 40px;
    font-weight: bold;
  }
  
  .purple {
    color: #6104df;
  }

  .blue {
    color: #826ef3;
  }
  
  .stats {
    padding: 60px 0;
    background-color: #3498db;
    color: white;
    text-align: center;
  }
  
  .contact-banner {
    padding: 80px 0;
    background-color: #3498dba8;
    text-align: center;
  }
  
  .footer {
    background-color: #2c3e50;
    padding: 40px 0;
    color: white;
    text-align: center;
  }
  
  .footer h1 {
    font-size: 36px;
  }
  </style>
  