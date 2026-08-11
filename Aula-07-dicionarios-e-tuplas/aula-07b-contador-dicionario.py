def ContadorLetras(string):
    contador = dict()
    for letra in string.upper():
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    return contador

print(ContadorLetras("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam et lacus a mi porta finibus. Etiam magna lectus, blandit tempor lacus eu, vehicula efficitur eros. Curabitur egestas lectus ut turpis tempus, in tincidunt leo commodo. Proin vestibulum finibus urna eu pulvinar. Mauris eu lorem a ipsum rutrum porta. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Integer pretium libero in tortor iaculis, quis tempus neque laoreet. Phasellus cursus, magna sed gravida viverra, orci neque cursus est, non elementum ex mauris eu arcu.

Donec dictum mauris eget egestas luctus. Sed ut ipsum aliquam, tincidunt felis ac, molestie velit. Pellentesque ornare ac purus nec fermentum. In ac finibus diam. Quisque est lectus, vulputate ac dignissim vitae, malesuada ut odio. Integer at justo a purus ultrices scelerisque in placerat ante. Donec ultricies viverra purus id bibendum. Praesent ut blandit nisi. Cras ut rutrum augue. Proin finibus justo nec venenatis imperdiet. Morbi egestas dolor massa, et ornare lectus tempor eu. Nam gravida lectus eget euismod bibendum. Donec luctus lectus urna, at dignissim orci sagittis eget. Duis sed venenatis ante, id rhoncus ligula. Quisque gravida magna maximus sapien iaculis gravida. Proin faucibus convallis diam tempus molestie.

Maecenas id mollis mauris. Ut turpis nulla, vestibulum non nisl ut, feugiat euismod odio. Mauris in quam quam. Nunc finibus finibus ipsum, nec ultrices risus rhoncus eu. Suspendisse hendrerit condimentum nisl, aliquam congue diam gravida tincidunt. Mauris bibendum lobortis turpis, vel dapibus felis hendrerit eget. Proin felis sem, euismod in aliquam eu, sollicitudin vitae nunc.

Nullam mauris metus, dignissim vitae tempus eu, dictum et odio. Quisque id ante eu justo maximus pharetra. Nunc porta magna diam, sed placerat nisl consequat ut. Ut vel diam condimentum, molestie libero nec, molestie nisi. Quisque tincidunt ornare dapibus. Etiam ut hendrerit erat. Nullam sagittis odio fermentum, aliquet sapien eget, molestie dolor. Vivamus ut velit pulvinar, sollicitudin metus faucibus, iaculis felis. Phasellus porttitor nunc a tortor ullamcorper condimentum ut vitae nisl. Donec sit amet dolor erat. Fusce vel orci porttitor, commodo nunc nec, facilisis justo. Aenean lobortis vestibulum felis, ut condimentum lacus. Proin congue sagittis purus tincidunt aliquet.

Aenean lacinia massa quis nunc ullamcorper, in rutrum justo condimentum. Aenean blandit, odio nec viverra dictum, lacus leo auctor ante, ac semper sapien nibh at nibh. Suspendisse finibus arcu nec est mattis, non condimentum libero semper. Aenean rutrum leo dui, quis varius lorem commodo in. Cras sodales, dolor in mattis porta, tellus velit iaculis felis, id pharetra libero ipsum ac nibh. Duis nec mauris a mi sagittis scelerisque sed nec enim. Duis augue nunc, placerat eget pretium maximus, placerat ac dui. Ut vel nibh ultricies, malesuada lectus in, aliquet urna. Duis tincidunt in ante nec dictum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam tincidunt aliquam massa id lacinia. Proin efficitur risus et nisl sagittis faucibus tempor id tellus. Aliquam erat volutpat. Vestibulum aliquet risus in congue aliquet."""))
