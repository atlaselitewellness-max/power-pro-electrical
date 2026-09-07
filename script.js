document.getElementById('year').textContent = new Date().getFullYear();

const navToggle = document.getElementById('nav-toggle');
const mainNav = document.getElementById('main-nav');

navToggle.addEventListener('click', () => {
  const isOpen = mainNav.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', String(isOpen));
});

mainNav.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    mainNav.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
  });
});

const contactForm = document.getElementById('contact-form');

contactForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const data = new FormData(contactForm);
  const name = data.get('name') || '';
  const replyTo = data.get('reply_to') || '';
  const message = data.get('message') || '';

  const subject = encodeURIComponent(`Enquiry from ${name} - Power Pro Electrical`);
  const body = encodeURIComponent(
    `Name: ${name}\nContact: ${replyTo}\n\n${message}`
  );

  window.location.href = `mailto:powerpro.co.za@gmail.com?subject=${subject}&body=${body}`;
});
