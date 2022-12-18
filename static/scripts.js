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
box.addEventListener('click', (event) => {
  if (event.target.id !== 'anime_waifu_img') {
    return;
  }
  testImgUrl();
});


// 이미지 로딩 시간이 너무 길다
// 원본 보기 기능이 있으면 좋겠다.