AOS.init();
/* 
data-aos="fade-up"
data-aos="fade-down"
data-aos="fade-left"
data-aos="fade-right"

data-aos="zoom-in"
data-aos="zoom-out"

fonte: https://michalsnik.github.io/aos/
npm: https://www.npmjs.com/package/aos
*/

function iniciarContadores() {
  const counters = document.querySelectorAll(".counter");

  const updateCount = (counter) => {
    const target = +counter.getAttribute("data-target");
    let currentCount = 0;
    const increment = 0.1; // quanto aumenta a cada passo (quanto menor, mais devagar)
    const delay = 15; // ms entre cada atualização (quanto maior, mais devagar)

    const interval = setInterval(() => {
      currentCount += increment;
      if (currentCount >= target) {
        counter.innerText = target.toFixed(0);
        clearInterval(interval);
      } else {
        counter.innerText = currentCount.toFixed(0);
      }
    }, delay);
  };

  const observer = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          updateCount(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  counters.forEach((counter) => {
    counter.innerText = "0";
    observer.observe(counter);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  iniciarContadores();
});
