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
  // Mapeamento de configuração por elemento (pode colocar mais se quiser)
  const configuracoes = [
    { seletor: ".contador-doacoes", incremento: 1, delay: 40 },
    { seletor: ".contador-pessoas", incremento: 50, delay: 15 }
  ];

  configuracoes.forEach(config => {
    const elemento = document.querySelector(config.seletor);
    if (!elemento) return;

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
}

document.addEventListener("DOMContentLoaded", iniciarContadores);
