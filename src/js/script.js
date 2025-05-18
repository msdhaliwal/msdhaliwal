// Set your target launch date
const launchDate = new Date();
launchDate.setFullYear(2025);
launchDate.setMonth(4); // May (0-indexed)
launchDate.setDate(25);
launchDate.setHours(0, 0, 0, 0);

function updateCountdown() {
  const now = new Date().getTime();
  const distance = launchDate.getTime() - now;

  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const hours = Math.floor((distance / (1000 * 60 * 60)) % 24);
  const minutes = Math.floor((distance / (1000 * 60)) % 60);
  const seconds = Math.floor((distance / 1000) % 60);

  document.getElementById("days").innerText = String(days).padStart(2, "0");
  document.getElementById("hours").innerText = String(hours).padStart(2, "0");
  document.getElementById("minutes").innerText = String(minutes).padStart(2, "0");
  document.getElementById("seconds").innerText = String(seconds).padStart(2, "0");

  if (distance < 0) {
    document.querySelector(".countdown").innerHTML = "Launched!";
  }
}

setInterval(updateCountdown, 1000);