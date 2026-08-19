document.addEventListener('DOMContentLoaded', () => {
    const audioPlayer = document.getElementById('audio-player');
    const mainPlayBtn = document.getElementById('main-play-btn');
    const playerTitle = document.getElementById('player-title');
    const playerArtist = document.getElementById('player-artist');
    const playButtons = document.querySelectorAll('.btn-play-stream');

    // Função para tocar uma música selecionada
    playButtons.forEach(button => {
        button.addEventListener('click', () => {
            const streamUrl = button.getAttribute('data-url');
            const title = button.getAttribute('data-title');
            const artist = button.getAttribute('data-artist');

            if (streamUrl && audioPlayer) {
                // 1. Atualiza a fonte do player invisível de áudio
                audioPlayer.src = streamUrl;
                audioPlayer.play();

                // 2. Atualiza o player no rodapé com os dados da música
                if (playerTitle) playerTitle.textContent = title;
                if (playerArtist) playerArtist.textContent = artist;
                if (mainPlayBtn) mainPlayBtn.textContent = '⏸';
            }
        });
    });

    // Controla o Play/Pause pelo botão do rodapé
    if (mainPlayBtn && audioPlayer) {
        mainPlayBtn.addEventListener('click', () => {
            if (!audioPlayer.src) return; // Se nenhuma música foi carregada ainda

            if (audioPlayer.paused) {
                audioPlayer.play();
                mainPlayBtn.textContent = '⏸';
            } else {
                audioPlayer.pause();
                mainPlayBtn.textContent = '▶';
            }
        });
    }
});