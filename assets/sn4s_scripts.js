window.addEventListener("DOMContentLoaded", function() { // on page DOMContentLoaded
  console.log('plugins loaded.')
  const sups = document.querySelectorAll('sup')
  sups.forEach(s => {
    s.addEventListener('click', event=> {
      alignSideNote(event.target);
    })
  });
});

function getOffset(el) {
  // get element's postion, left & top
  const rect = el.getBoundingClientRect();
  return {
    left: rect.left + window.scrollX,
    top: rect.top + window.scrollY
  };
}

function alignSideNote(t_footnote) {
  // align the side note y position according to the clicking footnote
  // and show it using style.opacity attrubute for fade-in effect
  let side_note_id = "footnote-" + t_footnote.innerText;
  //console.log('displaying', side_note_id)
  el_side_note = document.getElementById(side_note_id);
  align_position_top = (getOffset(t_footnote).top-10).toString() + "px";
  el_side_note.style.top = align_position_top;
  console.log(el_side_note)
  if (el_side_note.style.opacity == "" || el_side_note.style.opacity == "0") {
    el_side_note.style.opacity = "1";
  } else {
    el_side_note.style.opacity = "0";
  }
}
