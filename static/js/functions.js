// Abre/Fecha menu de ações da tabela
function toggleMenuActions(menuaction, element) {
    if ($(element).hasClass('menuActions--open')) {
        $('.menuActions').slideUp(300);
        $('.toggle-menuActions').removeClass('menuActions--open');
    } else {
        $('.menuActions').slideUp(300);
        $('.toggle-menuActions').removeClass('menuActions--open');
        $(element).addClass('menuActions--open');
        $(element).siblings('.menuActions').addClass('menuActions--open');
        $(element).siblings('.menuActions').slideDown(300);
    }
}

function abrirModal() {
    $('.modal').addClass('modal--open');
    $('body').addClass('modal--open');
}

function fecharModal() {
    $('.modal').removeClass('modal--open');
    $('body').removeClass('modal--open');
}

// Esconder / Mostrar testo de senha
function showHidePassword(element) {
    let elementAttr = $(element).siblings('.input-password').attr('type');
    let password = elementAttr == 'password' ? true : false;
    if (password) {
        $(element).siblings('.input-password').attr('type', 'text');
        $(element).siblings('.input-password').attr('placeholder', '123456');
    } else {
        $(element).siblings('.input-password').attr('type', 'password');
        $(element).siblings('.input-password').attr('placeholder', '******');
    }
    $(element).children('.showHidePassword__icon').toggleClass('hidden');
}