const CustomSlideContent = {
  id: "custom-slide-content", // Explicitly adding an id property

  init: function (reveal) {
    reveal.on("ready", (event) => {
      this.processData(event.currentSlide);
    });

    reveal.on("slidechanged", (event) => {
      this.processData(event.currentSlide);
    });
  },

  processData: function (slide) {
    if (slide.id === slideData.slideId) {
      const targetDiv = slide.querySelector("#" + slideData.targetDivId);
      if (targetDiv) {
        targetDiv.innerHTML = this.createList(slideData.items);
      }
    }
  },

  createList: function (items) {
    return `<ul>${items.map((item) => `<li>${item}</li>`).join("")}</ul>`;
  },
};
