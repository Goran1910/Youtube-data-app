import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { PlaylistService } from 'src/app/services/playlist.service';

@Component({
  selector: 'app-combo-albums',
  templateUrl: './combo-albums.component.html',
  styleUrls: ['./combo-albums.component.css']
})
export class ComboAlbumsComponent implements OnInit {

  channelTitle!: string | null;
  titles!: String[];
  selectedAlbum: string = 'all';

  @Output()
  selectedAlbumEmitter = new EventEmitter<string>();

  constructor(private playlistService: PlaylistService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.route.parent?.paramMap.subscribe((params) => {
      this.channelTitle = params.get('name');
      if(this.channelTitle){
        this.playlistService.getPlaylistsTitles(this.channelTitle).subscribe((titles) => {
          this.titles = titles;
        })
      }
    })
  }

  albumSelected(): void{
    this.selectedAlbumEmitter.emit(this.selectedAlbum);
  }

}
