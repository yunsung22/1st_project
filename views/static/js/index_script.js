// header, footer 고정
window.addEventListener('scroll', function() {
    var header = document.querySelector('header');
    var footer = document.querySelector('footer');

    if (window.scrollY > 0) {
        header.style.top = '0';
        footer.style.bottom = '0';
    } else {
        header.style.top = '-100px'; // 헤더의 높이만큼 이동
        footer.style.bottom = '-150px'; // 푸터의 높이만큼 이동
    }
});

// main 옷 정보
const clothingData = [
    { imageUrl: '옷1.jpg', title: '옷 제목 1' },
    { imageUrl: '옷2.jpg', title: '옷 제목 2' },
    { imageUrl: '옷3.jpg', title: '옷 제목 3' },
    // 추가적인 옷들의 정보가 있다면 이어서 추가합니다.
];

const clothingContainer = document.getElementById('clothing-items');

clothingData.forEach(item => {
    const clothingItem = document.createElement('div');
    clothingItem.classList.add('clothing-item');

    const image = document.createElement('img');
    image.src = item.imageUrl;
    clothingItem.appendChild(image);

    const title = document.createElement('h3');
    title.textContent = item.title;
    clothingItem.appendChild(title);

    clothingContainer.appendChild(clothingItem);
});


//여기부터 about자바스크립트
const sliderContainer = document.getElementById('slider-container');
let isDown = false;
let startX;
let scrollLeft;

sliderContainer.addEventListener('mousedown', (e) => {
    if (!e.target.closest('.slider-container')) return; // 슬라이더 컨테이너 내부에서 발생한 이벤트인지 확인
    isDown = true;
    startX = e.pageX - sliderContainer.offsetLeft;
    scrollLeft = sliderContainer.scrollLeft;
    sliderContainer.style.cursor = 'grabbing'; // 드래그 중일 때 커서 모양 변경
});

document.addEventListener('mouseup', () => {
    isDown = false;
    sliderContainer.style.cursor = 'grab'; // 드래그 종료 시 원래의 커서 모양으로 변경
});

document.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - sliderContainer.offsetLeft;
    const walk = (x - startX) * 3; // 스크롤 속도 조절
    sliderContainer.scrollLeft = scrollLeft - walk;
});


