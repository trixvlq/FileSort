import os

photo_file_types = ['jpg', 'jpeg', 'png', 'gif', 'tiff', 'bmp']
document_file_types = ['doc', 'docx', 'pdf', 'txt', 'rtf', 'odt']
video_file_types = ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv']

for entry in os.scandir('/other_files'):
    try:
        if entry.is_dir() and entry.name == '.idea':
            target_dir = '/projects'
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            os.replace(entry.path, f'{target_dir}/{entry.name}')
        elif entry.is_file():
            filetype = entry.name.split('.')[-1]

            if filetype == 'pptx' or 'ppt':
                target_dir = '/presentations'
            elif filetype in photo_file_types:
                target_dir = '/photos'
            elif filetype in document_file_types:
                target_dir = '/documents'
            elif filetype in video_file_types:
                target_dir = '/videos'
            elif filetype == 'zip':
                target_dir = '/archives'
            elif filetype == 'exe' and 'installer' in entry.name.lower():
                target_dir = '/installers'
            elif filetype == 'exe' and 'installer' not in entry.name.lower():
                target_dir = '/applications'
            elif filetype == 'torrent':
                target_dir = '/torrents'
            elif filetype == 'msi':
                target_dir = '/installation_packages'
            else:
                target_dir = '/other_files'

            if not os.path.exists(target_dir):
                os.mkdir(target_dir)

            os.replace(entry.path, f'{target_dir}/{entry.name}')

    except Exception as e:
        print(f"Error processing {entry.name}: {e}")
