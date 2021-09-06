import { Video } from "../Video";

export class BubbleSort{

    sort(videos: Video[], property: string, order: string){
        let p = property as keyof Video;
        for(var i = 0; i < videos.length; i++){
         
          for(var j = 0; j < ( videos.length - i -1 ); j++){
            if(order === 'asc'){
              if(videos[j][p] > videos[j+1][p]){
                var temp = videos[j]
                videos[j] = videos[j + 1]
                videos[j+1] = temp
              }
            } else if(order === 'desc'){
              if(videos[j][p] <= videos[j+1][p]){
                var temp = videos[j]
                videos[j] = videos[j + 1]
                videos[j+1] = temp
              }
            }
          }
        }
      }

}

