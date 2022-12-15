const box = document.getElementById('box');

const getImgUrl = () => {
  return fetch('/items')
    .then((response) => response.json())
    .then((data) => data.url);
};

const testImgUrl = async () => {
  anime_waifu_img.src = await getImgUrl();
};

const asyncTest = async () => {
  console.log('dsdsd');
};

testImgUrl();
box.addEventListener('click', () => {
  testImgUrl();
});
