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
  // Mapeamento de configuração por seletor
  const configuracoes = [
    { seletor: ".contador-doacoes", incremento: 1, delay: 90 },
    { seletor: ".contador-pessoas", incremento: 25, delay: 100 },
    { seletor: ".counter", incremento: 1, delay: 200 }
  ];

  configuracoes.forEach(config => {
    const elementos = document.querySelectorAll(config.seletor);
    if (!elementos.length) return;

    elementos.forEach(elemento => {
      const target = +elemento.getAttribute("data-target");
      let count = 0;

      const animar = () => {
        const timer = setInterval(() => {
          count += config.incremento;
          if (count >= target) {
            count = target;
            clearInterval(timer);
          }
          elemento.textContent = count;
        }, config.delay);
      };

      // Observer pra só começar quando aparecer na tela
      const observer = new IntersectionObserver(
        (entries, observer) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              animar();
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.2 }
      );

      observer.observe(elemento);
    });
  });
}

document.addEventListener("DOMContentLoaded", iniciarContadores);
