uxTitle = document.getElementById("ux-title");
container = document.getElementById("ux-wrapper");

if (uxTitle && container) {
  window.addEventListener("scroll", () => {
    uxSection();
  });

  window.addEventListener("resize", () => {
    uxSection();
  });
}

uxSection = () => {
  containerTop = container.getBoundingClientRect().y;
  containerheight = container.getBoundingClientRect().height;
  if (
    containerTop < 0 &&
    containerTop * -1 < containerheight - screen.height / 2
  ) {
    uxTitle.style.paddingTop = `${containerTop * -1 + 32}px`;
  }

  if (window.innerWidth < 879) {
    uxTitle.style.paddingTop = "";
    uxTitle.style.textAlign = "center";
    uxTitle.style.margin = "0 auto";
  } else {
    uxTitle.style.textAlign = "";
    uxTitle.style.margin = "";
  }
  console.log(window, container.getBoundingClientRect());
};
