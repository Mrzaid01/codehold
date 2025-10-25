const slides = document.querySelector('.slides');
const images = document.querySelectorAll('.slides img');
const prev = document.querySelector('.prev');
const next = document.querySelector('.next');
let index = 0;

function showSlide(i) {
  index = (i + images.length) % images.length;
  slides.style.transform = `translateX(${-index * 100}%)`;
}

prev.addEventListener('click', () => showSlide(index - 1));
next.addEventListener('click', () => showSlide(index + 1));

// Auto slide
setInterval(() => {
  showSlide(index + 1);
}, 3000);


const header = document.getElementById("main-header");

    window.addEventListener("scroll", function() {
      if (window.scrollY > 50) {
        header.classList.add("scroll-header");
        header.classList.remove("main-header");
      } else {
        header.classList.add("main-header");
        header.classList.remove("scroll-header");
      }
    });