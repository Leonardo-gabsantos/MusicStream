document.addEventListener('DOMContentLoaded', () => {
    const audioPlayer = document.getElementById('audio-player');
    const mainPlayBtn = document.getElementById('main-play-btn');
    const playerTitle = document.getElementById('player-title');
    const playerArtist = document.getElementById('player-artist');
    const playButtons = document.querySelectorAll('.btn-play-stream');
    const prevBtn = document.querySelector('.btn-step:first-child');
    const nextBtn = document.querySelector('.btn-step:last-child');

    // Elementos da Barra de Tempo
    const progressBar = document.getElementById('progress-bar');
    const currentTimeEl = document.getElementById('current-time');
    const totalDurationEl = document.getElementById('total-duration');

    let playlist = [];
    let currentIndex = -1;

    // Função para formatar segundos em mm:ss
    function formatTime(seconds) {
        if (isNaN(seconds)) return "0:00";
        const mins = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
    }

    // Mapeia todas as músicas da busca para a fila
    playButtons.forEach((button, index) => {
        const trackData = {
            url: button.getAttribute('data-url'),
            title: button.getAttribute('data-title'),
            artist: button.getAttribute('data-artist')
        };
        playlist.push(trackData);

        button.addEventListener('click', (e) => {
            e.stopPropagation();
            playTrack(index);
        });
    });

    function playTrack(index) {
        if (index < 0 || index >= playlist.length) return;

        currentIndex = index;
        const track = playlist[currentIndex];

        if (track && audioPlayer) {
            audioPlayer.src = track.url;
            audioPlayer.play();

            if (playerTitle) playerTitle.textContent = track.title;
            if (playerArtist) playerArtist.textContent = track.artist;
            if (mainPlayBtn) mainPlayBtn.textContent = '⏸';
        }
    }

    // Atualiza a barra de progresso e tempos durante a reprodução
    if (audioPlayer && progressBar) {
        audioPlayer.addEventListener('timeupdate', () => {
            if (audioPlayer.duration) {
                const progressPercent = (audioPlayer.currentTime / audioPlayer.duration) * 100;
                progressBar.value = progressPercent;

                // Preenchimento com a cor elegante #3b4252
                progressBar.style.background = `linear-gradient(to right, #3b4252 ${progressPercent}%, #404040 ${progressPercent}%)`;

                if (currentTimeEl) currentTimeEl.textContent = formatTime(audioPlayer.currentTime);
            }
        });

        audioPlayer.addEventListener('loadedmetadata', () => {
            if (totalDurationEl) totalDurationEl.textContent = formatTime(audioPlayer.duration);
        });

        // Permite ao usuário clicar/arrastar na barra para alterar o tempo
        progressBar.addEventListener('input', () => {
            if (audioPlayer.duration) {
                const seekTime = (progressBar.value / 100) * audioPlayer.duration;
                audioPlayer.currentTime = seekTime;
            }
        });
    }

    // Avançar
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            if (playlist.length === 0) return;
            const nextIndex = (currentIndex + 1) % playlist.length;
            playTrack(nextIndex);
        });
    }

    // Voltar
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            if (playlist.length === 0) return;
            if (audioPlayer.currentTime > 3) {
                audioPlayer.currentTime = 0;
            } else {
                const prevIndex = (currentIndex - 1 + playlist.length) % playlist.length;
                playTrack(prevIndex);
            }
        });
    }

    // Tocar Próxima Automática ao Terminar
    if (audioPlayer) {
        audioPlayer.addEventListener('ended', () => {
            if (playlist.length > 0) {
                const nextIndex = (currentIndex + 1) % playlist.length;
                playTrack(nextIndex);
            }
        });
    }

    // Play/Pause central
    if (mainPlayBtn && audioPlayer) {
        mainPlayBtn.addEventListener('click', () => {
            if (!audioPlayer.src) return;

            if (audioPlayer.paused) {
                audioPlayer.play();
                mainPlayBtn.textContent = '⏸';
            } else {
                audioPlayer.pause();
                mainPlayBtn.textContent = '▶';
            }
        });
    }

    // Curtir
    const likeButtons = document.querySelectorAll('.btn-like');
    likeButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            btn.classList.toggle('active');
        });
    });
});