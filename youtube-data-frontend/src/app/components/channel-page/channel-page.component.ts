import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-channel-page',
  templateUrl: './channel-page.component.html',
  styleUrls: ['./channel-page.component.css']
})
export class ChannelPageComponent implements OnInit {

  constructor(private route: ActivatedRoute, private router: Router) { }

  child!: String;


  ngOnInit(): void {
    
  }

  ngAfterViewInit(){
    let videoTable = document.querySelector('app-video-table');
    if(videoTable){
      document.querySelector('#videoNav')?.classList.add('pressed');
    } else{
      document.querySelector('#playlistNav')?.classList.add('pressed');
    }
    
  }

  public navigateToPlaylist(event: Event) {

    const queryParams: Params = { column: 'totalViews', order: 'desc', page: 1, album: 'All' };

    let elem = document.querySelector('#playlistNav');
    let classList = elem?.classList;
    if(!classList?.contains('pressed')){
      this.router.navigate(
        ['playlists'], 
        {
          relativeTo: this.route,
          queryParams: queryParams
      })
      elem?.classList.add('pressed');
    }
    document.querySelector('#videoNav')?.classList.remove('pressed');
    
  }

  public navigateToVideos(event: Event) {

    const queryParams: Params = environment.defaultQueryParams;
  
    let elem = document.querySelector('#videoNav');
    let classList = elem?.classList;
    if(!classList?.contains('pressed')){
      this.router.navigate(
        ['videos'], 
        {
          relativeTo: this.route,
          queryParams: queryParams 
      })
      
      elem?.classList.add('pressed');
      console.log(elem);
      
    }
    document.querySelector('#playlistNav')?.classList.remove('pressed');

  }

}
