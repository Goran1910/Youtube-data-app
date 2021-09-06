import  { Component, OnInit } from '@angular/core';
import { VideoService } from 'src/app/services/video.service';
import { Video } from 'src/app/Video';
import { Router, ActivatedRoute, Params } from '@angular/router';
import { MergeSort } from 'src/app/sorting-algs/MergeSort';
import { InsertionSort } from 'src/app/sorting-algs/InsertionSort';

@Component({
  selector: 'app-video-table',
  templateUrl: './video-table.component.html',
  styleUrls: ['./video-table.component.css']
})
export class VideoTableComponent implements OnInit {

  constructor(private videoService: VideoService, private route: ActivatedRoute, private router: Router) { }

  videos!: Video[];
  channelName!: string | null;
  order!: string;
  column!: string;
  page!: number;
  album: string = 'All';
  mergeSort!: MergeSort<Video>;
  insertionSort!: InsertionSort<Video>;

  ngOnInit(): void {

    this.mergeSort = new MergeSort()
    this.insertionSort = new InsertionSort();

    this.route.queryParams.subscribe((params) => {
      this.order = params.order;
      this.column = params.column; 
      this.page = params.page;
      this.album = params.album;
    });

    this.route.parent?.paramMap.subscribe((params) => {
      this.channelName = params.get('name');
      if (this.channelName != null) {
        this.videoService.getVideosByChannelName(this.channelName).subscribe((videos) => {
          this.videos = videos;
        });
        
      }
    });
  }

  changeColumnColor(){
    let currentlyHighlighted = document.querySelectorAll('.highlighted');
    currentlyHighlighted.forEach((ch) => ch.classList.remove('highlighted'));
    let elems = document.querySelectorAll(`td[data-column="${this.column}"]`);
    elems.forEach((elem) => elem.classList.add('highlighted'));
  }

  toggleCaretIcon() {
    let header = document.querySelector(`th[data-column="${this.column}"]`);
    let svgs = document.querySelectorAll(`svg`);
    svgs.forEach((svg) => svg.remove());
    if (header != null) {
      let inner = header.innerHTML;
      if(this.order === 'asc'){
        header.innerHTML = inner + ` <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-up-fill" viewBox="0 0 16 16">
        <path d="m7.247 4.86-4.796 5.481c-.566.647-.106 1.659.753 1.659h9.592a1 1 0 0 0 .753-1.659l-4.796-5.48a1 1 0 0 0-1.506 0z"/>
      </svg>`;
      } else{
        header.innerHTML = inner + ` <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-down-fill" viewBox="0 0 16 16">
          <path d="M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"/>
        </svg>`;
      }
    }
  }

  sortBy(property: string): void{
    
    if(this.isArraySortedInReverse(property)){
      this.order = this.order === 'asc' ? 'desc' : 'asc';
      this.mergeSort.sort(this.videos, 0, this.videos.length - 1, property, this.order);
    } else if(this.order === 'asc'){
      this.order = 'desc';
      this.insertionSort.sort(this.videos, property, this.order);
    } else{
      this.insertionSort.sort(this.videos, property, this.order);
    }
    this.column = property;
    
    this.changingQueryParams();
    this.changeColumnColor();
    this.toggleCaretIcon();
  }

  public changingQueryParams() {
    const queryParams: Params = { column: this.column, order: this.order, page: this.page, album: this.album };
  
    this.router.navigate(
      [], 
      {
        relativeTo: this.route,
        queryParams: queryParams, 
        queryParamsHandling: 'merge',
    })
  }

  albumChanged(selectedAlbum: string){
    this.album = selectedAlbum;
    this.column = 'views';
    this.order = 'desc';
    this.changingQueryParams();
    this.route.parent?.paramMap.subscribe((params) => {
      this.channelName = params.get('name');
      if (this.channelName != null) {
        if(this.album === 'All'){
          this.videoService.getVideosByChannelName(this.channelName).subscribe((videos) => {
            this.videos = videos;
          });
        } else{
          console.log(this.album);
          
          this.videoService.getVideosByPlaylistName(this.album).subscribe((videos) => {
            console.log(videos);
            
            this.videos = videos;
          });
        }
      }
    });
  }

  /*hide(video: Video): Boolean{
    if(this.album == 'All'){
      return false;
    }
    return video.playlist.title != this.album;
  }*/

  isArraySortedInReverse(property: String): Boolean{
    return this.column === property 
  }

  showBasedOnPage(index: number): Boolean{
    return (Math.floor(index / 50) + 1) != this.page;
  }

  nextPage(){
    this.page++;
    this.changingQueryParams();
  }

  previousPage(){
    this.page--;
    this.changingQueryParams();
  }

  isFirstPage(): Boolean{    
    return this.page == 1;
  }

  isLastPage(): Boolean{
    return this.page == (Math.floor(this.videos?.length / 50) + 1);
  }

  formatDuration(duration: number){
    let minutes = Math.floor(duration / 60);
    let seconds = duration - minutes * 60;
    return `${minutes}min ${seconds}sec`;
  }

  formatPercentages(number: number): String{
    return `${number}%`;
  }
}
