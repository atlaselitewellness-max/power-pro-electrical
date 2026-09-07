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
const formNote = document.getElementById('form-note');

const SUPABASE_URL = 'https://qzivwgmwtfwpkqhiblds.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF6aXZ3Z213dGZ3cGtxaGlibGRzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODg4MDg2MjEsImV4cCI6MjEwNDM4NDYyMX0.E0060iOJpqwZ587HigUOg2eqGz7p8BqArfUWG2xKegU';

contactForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const data = new FormData(contactForm);
  const name = data.get('name') || '';
  const replyTo = data.get('reply_to') || '';
  const message = data.get('message') || '';
  const submitBtn = contactForm.querySelector('button[type="submit"]');

  submitBtn.disabled = true;
  submitBtn.textContent = 'Sending…';

  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/leads`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
      },
      body: JSON.stringify({ name, contact: replyTo, message }),
    });
    if (!res.ok) throw new Error('save failed');

    contactForm.reset();
    formNote.textContent = "Thanks — we've got your details and will be in touch shortly.";
    formNote.style.color = '#f5b83d';
  } catch (err) {
    const subject = encodeURIComponent(`Enquiry from ${name} - Power Pro Electrical`);
    const body = encodeURIComponent(`Name: ${name}\nContact: ${replyTo}\n\n${message}`);
    window.location.href = `mailto:powerpro.co.za@gmail.com?subject=${subject}&body=${body}`;
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = 'Send Enquiry';
  }
});
